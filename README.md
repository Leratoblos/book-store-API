# book-store-API

Simple book store api
admin log details

user: admin
password: admin

end points

TO GET ALL BOOKS
http://127.0.0.1:8000/books/ GET 

TO DELETE A BOOK BY ID
http://127.0.0.1:8000/books/<ID NUMBER> / ie. http://127.0.0.1:8000/books/5
  
TO ADD A BOOK
  
 JSON SYNTAX IN BODY iD INCRIMENTED AUTOMATICALLY
   {
            "booktitle": "Think like a man",
            "author": "Steve Harvey",
            "description": "self help",
            "coverPrice": "349.99"
  }
        
