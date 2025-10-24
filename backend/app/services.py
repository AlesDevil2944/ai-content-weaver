# PASTE THIS ENTIRE CODE BLOCK INTO your blank backend/app/services.py file

import re
import json
import textstat
from openai import OpenAI
from markdownify import markdownify as md
from app.config import settings
from app.models import GenerateRequest, ContentType
import google.generativeai as genai
from app.config import settings # (This line should already be there)

# This line connects to OpenAI using your API key from the .env file
genai.configure(api_key=settings.GOOGLE_API_KEY)

class ContentService:

    # REPLACE your old generate_content function with this one

    def generate_content(self, req: GenerateRequest):
        """
        Main service function to generate and process content using Google Gemini.
        """
        # 1. Get the prompts
        system_prompt = self._get_system_prompt()
        user_prompt = self._get_user_prompt(req)

        # 2. Configure the Gemini model
        model = genai.GenerativeModel(
    model_name="gemini-1.0-pro",  # <--- CHANGE TO THIS
    system_instruction=system_prompt
)

        try:
            # 3. Call the AI
            response = model.generate_content(user_prompt)
            raw_content = response.text
        except Exception as e:
            print(f"Error calling Google AI: {e}")
            raise Exception("Failed to generate content from AI.")

        # 4. Extract HTML content and JSON metadata
        html_content, metadata = self._extract_content_and_meta(raw_content)

        if not html_content or not metadata:
            # Fallback if parsing fails
            html_content = "<p>Error: Failed to parse AI response. Please try again.</p>"
            metadata = {"meta_title": "Generation Error", "meta_description": "Failed to generate valid content."}

        # 5. Perform SEO analysis
        readability_score, readability_grade = self._analyze_seo(html_content)

        # 6. Convert to Markdown
        content_md = md(html_content)

        return {
            "content_html": html_content,
            "content_md": content_md,
            "meta_title": metadata.get("meta_title", "Generated Title"),
            "meta_description": metadata.get("meta_description", "Generated Description"),
            "readability_score": readability_score,
            "readability_grade": readability_grade
        }
    def _analyze_seo(self, html_content: str):
        """
        Calculates readability score.
        This is where future keyword analysis would go.
        """
        # Strip HTML tags for accurate text analysis
        plain_text = re.sub(r'<[^>]+>', ' ', html_content)
        plain_text = ' '.join(plain_text.split())
        
        if not plain_text:
            return 0.0, "N/A"
            
        # Flesch-Kincaid Readability Score
        score = textstat.flesch_reading_ease(plain_text)
        grade = textstat.flesch_kincaid_grade(plain_text)
        
        return score, f"Grade {grade}"

    def _extract_content_and_meta(self, raw_content: str):
        """
        Extracts the HTML content and the JSON metadata block.
        """
        html_content = ""
        metadata = {}
        
        # Regex to find the JSON block
        json_match = re.search(r"```json\s*(\{.*?\})\s*```", raw_content, re.DOTALL)
        
        if json_match:
            try:
                metadata = json.loads(json_match.group(1))
                # Get all content *before* the JSON block
                html_content = raw_content[:json_match.start()].strip()
            except json.JSONDecodeError:
                print("Failed to decode JSON from AI response")
                html_content = raw_content # Fallback
        else:
            # If no JSON block is found, return all content
            html_content = raw_content
            
        return html_content, metadata

    def _get_system_prompt(self) -> str:
        """
        Base instructions for the AI.
        """
        # This is the string that was broken before
        return """
You are an expert content creator and SEO specialist. Your task is to generate high-quality content based on a user's brief.

RULES:
1.  The main content MUST be formatted as a single, complete HTML block.
2.  Use a single <h1> for the main title.
3.  Use <h2> and <h3> tags for subheadings. DO NOT use <h4> or lower.
4.  Wrap all paragraphs in <p> tags.
5.  After the HTML content, you MUST provide a JSON block with metadata for the article.
6.  The JSON block must be formatted *exactly* like this:
    ```json
    {
      "meta_title": "A concise, SEO-friendly title (50-60 chars)",
      "meta_description": "A compelling meta description (150-160 chars)"
    }
    ```
"""

    def _get_user_prompt(self, req: GenerateRequest) -> str:
        """
        Generates the specific user-facing prompt.
        """
        prompt = f"""
Please generate the following piece of content:

-   **Topic Brief:** {req.brief}
-   **Content Type:** {req.content_type.name}
-   **Tone:** {req.tone.value}
-   **Target Length:** Approximately {req.length} words.
"""
        
        if req.content_type == ContentType.blog:
            prompt += "\n**Specific Instructions:** Write an informative, well-structured blog post. Focus on providing value and answering the user's brief. Use clear headings and lists where appropriate."
        elif req.content_type == ContentType.promo:
            prompt += "\n**Specific Instructions:** Write a persuasive promotional article. Focus on benefits, include a clear call-to-action (CTA), and use an engaging, persuasive tone."
        elif req.content_type == ContentType.creative:
             prompt += "\n**Specific Instructions:** Write a creative piece (e.g., a short story, poem, or narrative). Focus on originality, voice, and imagery."

        return prompt

# Create a single instance for the router to use
content_service = ContentService()