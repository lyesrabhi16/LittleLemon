###APIs:

# Create user
```
POST http://localhost:8000/auth/users/ with body
email
username
password
```

# get token
```
POST http://localhost:8000/api-token-auth/ with body
username
password
```
# check auth
```
GET http://localhost:8000/auth/users/me with Auth
PREFIX: Token
TOKEN: token received from get token
```

# menu api
list many and create endpoint: http://localhost:8000/restaurant/menu
list one, update and destroy endpoint: http://localhost:8000/restaurant/menu/:id

# booking api
endpoint: http://localhost:8000/restaurant/booking/tables

book: 
```
POST http://localhost:8000/restaurant/booking/tables with body
Name
No_of_guests
BookingDate with this format YYYY-MM-DD
```