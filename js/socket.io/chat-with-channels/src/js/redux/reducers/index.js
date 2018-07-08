
import { combineReducers } from 'redux'

import channels from './channels'
import messages from './messages'


const rootReducer = combineReducers({
    channels,
    messages,
})

export default rootReducer
