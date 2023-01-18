# psearch 

Provenance search over ASKEM Entities using GPT-3.

***HIGHLY EXPERIMENTAL; NO GUARANTEES***

See some basic tests at [tests.log.md](./tests.log.md). 

## TODOs
- [ ] Tweak parameters passed to OpenAI, particularly `temperature`.
- [ ] Enumerate more example queries for testing
- [ ] Enumerate more queries for the preamble to GPT-3
- [ ] Investigate possible heuristics pre and post query
- [ ] Refactor psearch [VERY LOW PRIORITY ATM]

## Usage

Setup with 
```
poetry install
```

**psearch** also depends on a file `openai-auth.json` which contains:
```
{
        "token": "sk-..." 
}
```

where `sk-...` is replaced by your OpenAI key.

Use with
```
poetry run psearch "Your directive or question here"
```

and an openCypher query will (hopefully) be returned.


## run the ui
To run the ui that connects to TDS run these commands from the command line
```
cd ui
npm install
npm run serve
```