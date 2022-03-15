## Default instrument and resolution

Change the default symbol (instrument) and resolution (time interval).

Minimum supported resolution is 1 second.

[symbol, interval](Widget-Constructor.md#symbol-interval)

## Default visible range (timeframe)

Change time range of bars for the default resolution

[timeframe](Widget-Constructor.md#timeframe)

## Default visible range for resolutions

Change time range of bars when the resolution is changed by the user. A sample is available here:

[onIntervalChanged()](Chart-Methods.md#onintervalchanged)

## Initial timezone

You can set the default timezone. It can be changed by the user in the menu.

[timezone](Widget-Constructor.md#timezone)

## Chart colors

Customize the colors of the chart so that it matches your site design.

1. [Toolbar color](Toolbars.md)
1. Chart color at the start - [overrides](Widget-Constructor.md#overrides), on the fly - [Chart Style properties](Chart-Style-Properties.md)
1. [CSS Color Themes](CSS-Color-Themes.md)

## Default properties of a chart

You can change any available properties in the properties dialog.

1. [Initially](Widget-Constructor.md#overrides)
1. [On the fly](Widget-Methods.md#applyoverridesoverrides)

## Show/hide chart elements

Certain chart elements (toolbars, buttons, other controls) can be hidden if you don't need them.

1. Most of the chart elements can be shown/hidden by using [Featuresets](Featuresets.md)
1. You can add [your own CSS](Widget-Constructor.md#custom_css_url)

## Initial list of favorite intervals / chart styles

You can select the intervals and chart styles that will be shown in the top toolbar by default. A user can change it if `items_favoriting` is enabled in the [Featuresets](Featuresets.md).

[favorites](Widget-Constructor.md#favorites)

## Resolutions that are displayed in the menu

1. The complete [list of resolutions](JS-Api.md#supported_resolutions) is provided in the configuration of the datafeed
1. Resolutions are enabled or disabled in the list being based on the [symbol information](Symbology.md#supported_resolutions)
1. Initial list of favorite resolutions [can be adjusted](Widget-Constructor.md#favorites)

## Context menu

You can add new elements to the context menu or hide the existing items.

[onContextMenu(callback)](Widget-Methods.md#oncontextmenucallback)
