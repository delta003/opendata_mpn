# OpenData MPN

A different API for open data on educational institutions in Serbia provided by the Ministry of Education, Science and Technological Development of the Republic of Serbia.

API is defined in `api/api.yml`

### Output

Output is in `data` folder. To generate output, run `src/main.py`

### Development

API is defined in [Conjure](https://palantir.github.io/conjure/#/readme). Repository contains `conjure` compiler and
`conjure-python` generator. To regenerate API after update, run `generate-api.sh` script.
