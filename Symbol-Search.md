The Symbol Search is used to search and display instruments that match a full or partial instrument name entered in the search field.

## Setting data

If you have a short list of symbols, the easiest way to display them in the symbol search is to implement the [symbols group request API](UDF.md#symbol-group-request).

Otherwise, you can use a [single symbol search requests](UDF.md#symbol-search).

In case of JS API, you need to implement [searchSymbols](JS-Api.md#searchsymbolsuserinput-exchange-symboltype-onresultreadycallback).

## Filters

The search window has predefined UI to filter symbols based on [symbol types](JS-Api.md#symbols_types) and [exchanges](JS-Api.md#exchanges).
Both filters are optional. You can use any string as a symbol type.

## Grouping of symbols

The search window displays symbols grouped by a root. To enable grouping you need to [provide a object with regular expressions](JS-Api.md#symbols_grouping) to parse instrument names.

## Hiding the Symbol Search

If your use of the library doesn't involve changing the displayed instrument by users, then you can hide the search box using [header_symbol_search](Featuresets.md) featureset.
