import domain
from fastapi import FastAPI

app = FastAPI()


@app.get("/youngers/{n}")
async def get_youngers(n: int):
    return domain.youngers(n)


@app.get("/olders/{n}")
async def get_olders(n: int):
    return domain.olders(n)


@app.get("/gender-distribution")
async def get_distribution():
    return domain.gender_distribution()


@app.get("/people/{cpf_without_pountuation}")
async def get_people_cpf(cpf_without_pountuation: int):
    return domain.get_people(cpf_without_pountuation)


@app.get("/blood-types/stats")
async def get_blood_types():
    return domain.blood_types()


@app.get("/peoples")
async def get_peoples():
    return domain.peoples()


@app.get("/peoples/search")
async def get_peoples(q:str):
    return domain.people_search(q)
