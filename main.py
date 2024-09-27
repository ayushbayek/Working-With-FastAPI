from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {"data":"blog list"}


@app.get('/blog/unpublished')
def unpublished():
    # fetch unpublished blogs
    return {"data":"unpublished blogs"}


# parenthesis is used for dynamic paths
@app.get('/blog/{id}')
def show(id : int):   # type validation is done using pydantic as FastAPI uses it
    # fetch blog with the given id
    return {"data":id}


@app.get('/blog/{id}/comments')
def comments(id : int):
    # will fetch all the comments for a given blog
    return {"data":{"comments":['list of comments']}}