/* PASTE THIS CODE INTO frontend/src/components/GeneratorForm.jsx */

import React, { useState } from 'react'

const GeneratorForm = ({ onGenerate, isLoading }) => {
  const [brief, setBrief] = useState('')
  const [contentType, setContentType] = useState('informative_blog')
  const [tone, setTone] = useState('Professional')
  const [length, setLength] = useState(500)

  const handleSubmit = (e) => {
    e.preventDefault()
    onGenerate({
      brief,
      content_type: contentType,
      tone,
      length: parseInt(length, 10),
    })
  }

  return (
    <form onSubmit={handleSubmit}>
      <div className="form-group">
        <label htmlFor="brief">Content Brief</label>
        <textarea
          id="brief"
          value={brief}
          onChange={(e) => setBrief(e.target.value)}
          placeholder="e.g., 'A blog post about the benefits of Python FastAPI...'"
          required
        />
      </div>

      <div className="form-group">
        <label htmlFor="contentType">Content Type</label>
        <select
          id="contentType"
          value={contentType}
          onChange={(e) => setContentType(e.target.value)}
        >
          <option value="informative_blog">Informative Blog Post</option>
          <option value="promotional_article">Promotional Article</option>
          <option value="creative_writing">Creative Writing</option>
        </select>
      </div>

      <div className="form-group">
        <label htmlFor="tone">Tone of Voice</label>
        <select id="tone" value={tone} onChange={(e) => setTone(e.target.value)}>
          <option value="Professional">Professional</option>
          <option value="Casual">Casual</option>
          <option value="Witty">Witty</option>
          <option value="Persuasive">Persuasive</option>
        </select>
      </div>

      <div className="form-group">
        <label htmlFor="length">Target Length (words)</label>
        <input
          id="length"
          type="number"
          step="50"
          value={length}
          onChange={(e) => setLength(e.target.value)}
        />
      </div>

      <button type="submit" disabled={isLoading}>
        {isLoading ? 'Generating...' : 'Weave Content'}
      </button>
    </form>
  )
}

export default GeneratorForm