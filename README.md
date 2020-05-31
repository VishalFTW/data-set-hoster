# data-set-hoster


Fill out a simple python object, host the results!

Example
-------

Create this class...

```python
class MBArtistCreditFuzzyQuery(Query):

    def __init__(self, db_connect_str):
        self.db_connect_str = db_connect_str
        self.index = None

    def setup(self):
        self.index = create_artist_credit_tree()

    def names(self):
        return ("mb-artist-credit-fuzzy", "MusicBrainz artist credit fuzzy lookup query")

    def inputs(self):
        return ['distance', 'artist_credit_name']

    def outputs(self):
        return ['distance', 'artist_credit_name', 'artist_credit_id']

    def fetch(self, params, offset=-1, limit=-1):
        if limit < 1:
            limit = DEFAULT_LIMIT

        node = ArtistCreditNode(params['artist_credit_name'].strip().lower(), 0)
        results = []
        for distance, node in self.index.find(node, int(params['distance']))[:limit]:
            results.append({ 'distance': distance, 
                             'artist_credit_name': node.artist_credit_name, 
                             'artist_credit_id': node.artist_credit_id })

        return results
```

and get this web page:

![Demo web page](/misc/web-page.png)
