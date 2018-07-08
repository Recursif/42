
import history from '../../history'


/**
 * ACTION GET /channel/add
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
                        channels: json.channels,
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


/**
 * ACTION POST /channel/add
 * Action to add a new channel
 */
export const addChannel = (channelName) => {
    return (dispatch) => {
        dispatch({
            type: 'CLEAR_MESSAGES'
        })
        return fetch('/channels', {
            method: 'post',
            headers: { 'Content-Type': 'application/json' },
            body: {
                channelName: channelName,
            },
        }).then((response) => {
            if (response.ok) {
                return response.json().then((json) => {
                    dispatch({
                        type: 'ADD_CHANNEL',
                        channel: json.channel,
                    })
                    history.push("/channel/" + channel._id)
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
