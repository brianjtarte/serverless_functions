# LAB 16
## Project: Serverless
### Author: Brian Tarte
#### Collaborator(s): Brendon Hampton



**Links and Resources:**
[Vercel Link](https://serverless-functions-blue.vercel.app/api/app?name=peru)

### Feature Tasks and Requirements
- [x] Sign up with Vercel.
- [x] Create a repository on Github and link it to Vercel account.
- [x] Use requests library to interact with REST Countries API
- [x] Create a serverless function following Vercel’s get-started directions that handles two kinds of queries:
- [x] The serverless function should handle a GET http request with a given country name that responds with a string with the form The capital of X is Y
- [x] E.g./capital-finder?country=Chile should generate an http response of The capital of Chile is Santiago.
- [] The serverless function should handle a GET http request with a given capital that responds with a string with the form The capital of X is Y
- [] E.g./capital-finder?capital=Santiago should generate an http response of Santiago is the capital of Chile.
### Setup

**Initialize application:** 
- Local: vercel dev (in terminal, gives you local development environment)
- After localhost:3000/ link is generated, must add api/app?name='insert name of any country here'


