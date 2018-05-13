import React from 'react'
import { hydrate } from 'react-dom'
import App from '../shared/App'

hydrate(
  <App data={window.__INITIAL_DATA__}/>
  document.getElementByID('app')
)


/*

This will adding event listeners and interactivity


*/
