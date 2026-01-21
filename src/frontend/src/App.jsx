import { useState, useEffect } from 'react'
import api from './api/api'
import './App.css'

function App() {
  const [health, setHealth] = useState('Loading...')
  const [error, setError] = useState(null)

  useEffect(() => {
    api.get('/api/health')
      .then(response => {
        setHealth(response.data.message || response.data.status)
      })
      .catch(err => {
        console.error(err);
        setError(`Failed to connect to backend: ${err.message}`)
      })
  }, [])

  return (
    <div style={{ textAlign: 'center', marginTop: '50px' }}>
      <h1>Portfolio Full-Stack Test</h1>
      <div style={{ padding: '20px', border: '1px solid #ccc', display: 'inline-block', borderRadius: '8px' }}>
        <h2>Backend Status:</h2>
        {error ? (
          <p style={{ color: 'red', fontWeight: 'bold' }}>{error}</p>
        ) : (
          <p style={{ color: 'green', fontWeight: 'bold' }}>{health}</p>
        )}
      </div>
    </div>
  )
}

export default App
