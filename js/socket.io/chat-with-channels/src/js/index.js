
import React from 'react'
import ReactDOM from 'react-dom'
import { Provider } from 'react-redux'
import { Router } from 'react-router-dom'
import configureStore from './store'
import App from './App'
import history from './history'

const initialState = {
    auth: {},
    messages: {}
}

const store = configureStore(initialState)

ReactDOM.render(
    <Provider store={store}>
        <Router history={history}>
            <App />
        </Router>
    </Provider>,
    document.getElementById("app")
)