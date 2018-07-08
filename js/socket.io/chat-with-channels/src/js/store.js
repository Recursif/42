
import { applyMiddleware, createStore } from 'redux'
import { createLogger } from 'redux-logger'
import thunk from 'redux-thunk'
import promise from 'redux-promise'
import rootReducer from './redux/reducers'

const configureStore = () => {
    const logger = createLogger()

    const store = createStore(
        rootReducer,
        applyMiddleware(thunk, promise, logger)
    )

    return store
}

export default configureStore