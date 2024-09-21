
# Parent registration json

{
    "user": {
        "username": "parent123",
        "first_name": "John",
        "last_name": "Doe",
        "email": "john.doe@example.com",
        "password": "password123"
    },
    "address": "123 Main Street, Townsville",
    "phone_number": "234567890",
    "gender": "M",
    "children": [
        {
            "first_name": "Sam",
            "last_name": "John",
            "age": 15,
            "class_id": 2,        
            "gender": "M"
        },
        {
            "first_name": "Tom",
            "last_name": "John",
            "age": 5,
            "class_id": 1,        
            "gender": "M"
        }
    ]
}


{
    "user": {
        "username": "parent456",
        "first_name": "Alice",
        "last_name": "Smith",
        "email": "alice.smith@example.com",
        "password": "password123"
    },
    "address": "456 Elm Street, Newtown",
    "phone_number": "987654321",
    "gender": "F",
    "children": [
        {
            "first_name": "Liam",
            "last_name": "Smith",
            "age": 10,
            "class_id": 3,
            "gender": "M"
        },
        {
            "first_name": "Emma",
            "last_name": "Smith",
            "age": 7,
            "class_id": 2,
            "gender": "F"
        }
    ]
}


# Add children details

{
    "first_name": "Sam",
    "last_name": "John",
    "age": 15,
    "class_id": 2,        
    "gender": "M",
    "parent": 14            
}


# Teacher Registration

{
    "user": {
        "username": "samjohn",
        "first_name": "Sam",
        "last_name": "John",
        "email":"ghkk@gmail.com",
        "password": "password123"
    },
    "gender": "M",
    "class_id": 1  
}


#pip install djangorestframework-simplejwt