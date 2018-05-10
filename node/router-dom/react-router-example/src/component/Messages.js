import React from 'react';

import { Link } from 'react-router-dom';

const Messages = () => (
  <div>
    <h2>Messages</h2>
    <ul>
    {
      [...Array(5).keys()].map(n => {
        return <li key={n}>
          <Link to={`${match.url}/${n+1}`}>
            Messages {n+1}
          </Link>
          </li>;
      })
    }
    </ul>
    <Route path={`{match.url}/:id`} component={Message} />
  </div>
);

export default Messages;
