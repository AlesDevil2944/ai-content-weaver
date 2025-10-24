/* PASTE THIS CODE INTO frontend/src/components/ContentDisplay.jsx */

import React from 'react'

const ContentDisplay = ({ content, isLoading, error }) => {

  const downloadFile = (data, filename, type) => {
    const blob = new Blob([data], { type })
    const url = URL.createObjectURL(blob)
    const a = document.createElement('a')
    a.href = url
    a.download = filename
    document.body.appendChild(a)
    a.click()
    document.body.removeChild(a)
    URL.revokeObjectURL(url)
  }

  const handleExportHTML = () => {
    if (content) {
      downloadFile(
        content.content_html,
        `${content.meta_title.slice(0, 20)}.html`,
        'text/html'
      )
    }
  }

  const handleExportMD = () => {
    if (content) {
      downloadFile(
        content.content_md,
        `${content.meta_title.slice(0, 20)}.md`,
        'text/markdown'
      )
    }
  }

  if (isLoading) {
    return (
      <div className="content-display">
        <div className="loading-placeholder">Generating... Please wait.</div>
      </div>
    )
  }

  if (error) {
    return (
      <div className="content-display">
        <div className="loading-placeholder" style={{ color: '#ff8a8a' }}>
          <strong>Error:</strong> {error}
        </div>
      </div>
    )
  }

  if (!content) {
    return (
      <div className="content-display">
        <div className="loading-placeholder">
          Your generated content will appear here.
        </div>
      </div>
    )
  }

  return (
    <div className="content-display">
      <div className="seo-bar">
        <div className="seo-item">
          <strong>Meta Title:</strong> <span>{content.meta_title}</span>
        </div>
        <div className="seo-item">
          <strong>Meta Desc:</strong> <span>{content.meta_description}</span>
        </div>
        <div className="seo-item">
          <strong>Readability:</strong> 
          <span>
            {content.readability_score.toFixed(1)} (Grade:{' '}
            {content.readability_grade})
          </span>
        </div>
      </div>
      <div className="content-output">
        <div
          className="content-output-inner"
          dangerouslySetInnerHTML={{ __html: content.content_html }}
        />
      </div>
      <div className="export-buttons">
        <button onClick={handleExportHTML}>Export as .html</button>
        <button onClick={handleExportMD}>Export as .md</button>
      </div>
    </div>
  )
}

export default ContentDisplay