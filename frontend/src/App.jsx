/* PASTE THIS CODE INTO frontend/src/App.jsx */

import { useState } from 'react'
import axios from 'axios'
import GeneratorForm from './components/GeneratorForm'
import ContentDisplay from './components/ContentDisplay'
import './index.css' // We import index.css, NOT App.css

// Configure your API base URL
const API = axios.create({
  baseURL: 'http://localhost:8000/api/v1',
})

function App() {
  const [content, setContent] = useState(null)
  const [isLoading, setIsLoading] = useState(false)
  const [error, setError] = useState(null)

  const handleGenerate = async (formData) => {
    setIsLoading(true)
    setError(null)
    setContent(null)
    
    try {
      const response = await API.post('/generate', formData)
      setContent(response.data)
    } catch (err) {
      console.error(err)
      setError(
        err.response?.data?.detail || 'An unexpected error occurred.'
      )
    } finally {
      setIsLoading(false)
    }
  }

  return (
    <>
      <h1>AI Content Weaver 🤖</h1>
      <div className="app-container">
        <div className="form-container">
          <GeneratorForm onGenerate={handleGenerate} isLoading={isLoading} />
        </div>
        <div className="content-container">
          <ContentDisplay 
            content={content} 
            isLoading={isLoading} 
            error={error} 
          />
        </div>
      </div>
    </>
  )
}

export default App