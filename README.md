Part 1 - Python Function
Part 1 Output
[{'user_id': 'u1', 'channel': 'email', 'message': 'Hello, I want info about grants for education.', 'category': 'grant_search'}, {'user_id': 'u3', 'channel': 'email', 'message': 'Please send the report again.', 'category': 'report_request'}, {'user_id': 'u1', 'channel': 'whatsapp', 'message': 'Can you help me find funding?', 'category': 'grant_search'}, {'user_id': 'u4', 'channel': 'telegram', 'message': 'Good morning!', 'category': 'unknown'}, {'user_id': 'u5', 'channel': 'email', 'message': 'Can you send me the scholarship document?', 'category': 'grant_search'}]

Conflict resolution:

If a message matches more than one rule I will prioritize in the order grant search, report request, general questions.

Part 2

what's wrong, why it matters, and ,how you'd fix it

1.Hard coded API
If the code is shared key can be stolen
Store API key as an environment variable. Example: using a .env file

2.User input is directly concatenated in to SQL query
Users can manipulated SQL statement to get unintended data
Use parameterized queries instead of string concat

3.ask_llm() is called twice
This does API calls twice, which makes it slower
Store answer in a variable and reuse it 

4.Sends all document content to llm
The prompt may be very large and can be expensive
Trim the context

Part 3

Q1. LIKE '%...%' search becomes slow because postgres need to scan full documents tables. I would suggest to use Postgres full text seach hich will create a searchable index of words in the documents so matching document can be find faster

Q2. By sending all documents to the llm prompt becomes very large. It increases cost, becomes slow and may exceed the models context limit. A basic RAG approach would split documents into smaller chunks, convert each chunk into embeddings and store them in a database. When a user asks a question the system finds the top-k most relevant chunks using similarity search and sends only those chunks to the llm

Q3.
Network timeout. The API server may be too slow, the internet connection may be down. Set a timeout, Retry the request
API return an error - Invalid API. Has to check status code and handle the error
Rate limiting - Because too many requests were sent in a short period. Wait and retry after a delay

Q4.
I would create a users table to store user information (user_id,name,email,created_date)and a messages table (message_id,user_id,message,created_date)to store chat history


Time Spent - Approximately 4 hours, including researching a few concepts





