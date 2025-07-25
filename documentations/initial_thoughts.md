#### Proposition: 
Build a personalized chat box, where each user can attach a specific context to the chat so that the chat bot can retrieve information from the context and give a better answer.

#### Components:
- A `User Management System` (ums) which will be self managed as of now
    - SignUp -> Creating a partially completed profile
    - SignIn -> Validating the profile and entry to the console with a session
    - SignOut -> Invalidating Session
    - Delete -> Invalidating Profile
- A `Chat Management System` (chatms)
    - Create a new chat per user
        - which assigns a fresh chatbot to each chat session
    - Delete a chat per user
    - Clear chat history
- A `Context Management System` (ctxms)
    - Create new context(s) per user
    - Delete context(s) per user
    - Delete all contexts per user
- A console combines all of them above, ums + chatms + ctxms