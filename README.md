# OpenData MPN

A different API for [open data on educational institutions in Serbia](http://opendata.mpn.gov.rs/index.php?page=ustanove)
provided by Ministry of Education and Science.

API is defined in `api/api.yml`

### Output

Output is in `data` folder. To generate output, run `src/main.py`

### Development

API is defined in [Conjure](https://palantir.github.io/conjure/#/readme). Repository contains `conjure` compiler and
`conjure-python` generator. To regenerate API after update, run `generate-api.sh` script.
