#!/usr/bin/env python3
import json
from typing import List, Union, Optional
from uuid import UUID

from markupsafe import Markup
from pydantic import BaseModel

from datasethoster import Query


class ExampleInput(BaseModel):
    number: int
    num_lines: int


class OutputComment(BaseModel):
    comment: str


class OutputData(BaseModel):
    listened_at: str
    duration: int
    difference: Optional[int]
    skipped: Optional[int]
    artist_name: str
    track_name: str
    recording_mbid: Optional[UUID]


ExampleOutput = Union[OutputComment, OutputData]


class ExampleQuery(Query[ExampleInput, ExampleOutput]):

    def setup(self):
        pass

    def names(self):
        return "example", "Useless arithmetic table example"

    def introduction(self):
        return """This is the introduction, which could provide more useful info that this introduction does."""

    def inputs(self):
        return ExampleInput

    def outputs(self):
        return ExampleOutput

    def fetch(self, params: List[ExampleInput], offset=-1, count=-1):
        with open("/app/data.json") as f:
            data = json.load(f)
        results = []
        for item in data:
            if item["type"] == "markup":
                results.append(OutputComment(comment=Markup(item["data"])))
            else:
                for x in item["data"]:
                    results.append(OutputData(**x))
        return results
