import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import Menu from './components/Menu/Menu'
import Statistics from './components/Statistics/Statistics'
import Futamigo from '/src/assets/futamigo_resized.png'
import Futl from './components/Futl/Futl'
import './App.css'
import './components/Menu/Menu.css'
import './components/Statistics/Statistics.css'
import './components/Futl/Futl.css'

function App() {
  const [count, setCount] = useState(0)
  const [currentIndex, setCurrentIndex] = useState(0);

  return (
    <>
      <div className='header'>
        <h1>FUTAMIGO</h1>
        <img src={Futamigo} alt="Futamigo Logo" />
      </div>
      <Menu currentIndex={currentIndex} setCurrentIndex={setCurrentIndex}/>
      <div className='content'>
        {currentIndex === 0 ? null : null}
        {currentIndex === 1 ? <Statistics/> : null}
        {currentIndex === 2 ? null : null}
        {currentIndex === 3 ? null : null}
        {currentIndex === 4 ? <Futl/> : null}
        {currentIndex === 5 ? null : null}
      </div>
      <div className='footer'>

      </div>
    </>
  )
}

export default App
