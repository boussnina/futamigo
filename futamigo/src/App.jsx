import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import Menu from './components/Menu/Menu'
import './App.css'

function App() {
  const [count, setCount] = useState(0)
  const [currentIndex, setCurrentIndex] = useState(0);

  return (
    <>
      <div className='header'>
        <h1>FUTAMIGO</h1>
      </div>
      <div className='content'>
        <Menu currentIndex={currentIndex} setCurrentIndex={setCurrentIndex}/>
      </div>
      <div className='footer'>

      </div>
    </>
  )
}

export default App
