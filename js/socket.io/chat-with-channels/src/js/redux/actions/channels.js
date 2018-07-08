
import history from '../../history'


/**
 * ACTION GET /channels
 * Action to get channels

 */
export const fetchChannels = () => {
    return (dispatch) => {
        dispatch({
            type: 'CLEAR_MESSAGES'
        })
        return fetch('/channels', {
            method: 'get',
            headers: { 'Content-Type': 'application/json' },
        }).then((response) => {
            if (response.ok) {
                return response.json().then((json) => {
                    dispatch({
                        type: 'ADD_FETCHED_CHANNELS',
                        tickets: json.tickets,
                    })
                })
            } else {
                return response.json().then((json) => {
                    dispatch({
                        type: 'ADD_CHANNELS_FAILURE',
                        messages: Array.isArray(json) ? json : [json]
                    })
                })
            }
        })
    }
}
