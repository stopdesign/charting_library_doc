Below is the list of methods that the widget supports. You can call them using the widget object that is returned to you by the widget's constructor.

**Remark**: Please note that it's safe to call any method only **after** onChartReady callback function is called.

Example:

```javascript
widget.onChartReady(function() {
    // It's now safe to call any other methods of the widget
});
```

## Methods

* [Subscribing To Chart Events](#subscribing-to-chart-events)
  * [onChartReady(callback)](#onchartreadycallback)
  * [headerReady()](#headerready)
  * [onGrayedObjectClicked(callback)](#ongrayedobjectclickedcallback)
  * [onShortcut(shortcut, callback)](#onshortcutshortcut-callback)
  * [subscribe(event, callback)](#subscribeevent-callback)
  * [unsubscribe(event, callback)](#unsubscribeevent-callback)
* [Chart Actions](#chart-actions)
  * [chart()](#chart)
  * [getLanguage()](#getlanguage)
  * [setSymbol(symbol, interval, callback)](#setsymbolsymbol-interval-callback)
  * [remove()](#remove)
  * [closePopupsAndDialogs()](#closepopupsanddialogs)
  * [selectLineTool(drawingId)](#selectlinetooldrawingid)
  * [selectedLineTool()](#selectedlinetool)
  * [takeScreenshot()](#takescreenshot)
  * [takeClientScreenshot()](#takeclientscreenshotoptions)
  * [lockAllDrawingTools](#lockalldrawingtools)
  * [hideAllDrawingTools](#hidealldrawingtools)
  * [magnetEnabled](#magnetenabled)
  * [magnetMode](#magnetmode)
  * [startFullscreen](#startfullscreen)
  * [exitFullscreen](#exitfullscreen)
* [Saving/Loading Charts](#savingloading-charts)
  * [save(callback)](#savecallback)
  * [load(state)](#loadstate)
  * [getSavedCharts(callback)](#getsavedchartscallback)
  * [loadChartFromServer(chartRecord)](#loadchartfromserverchartrecord)
  * [saveChartToServer(onCompleteCallback, onFailCallback, options)](#savecharttoserveroncompletecallback-onfailcallback-options)
  * [removeChartFromServer(chartId, onCompleteCallback)](#removechartfromserverchartid-oncompletecallback)
* [Custom UI Controls](#custom-ui-controls)
  * [onContextMenu(callback)](#oncontextmenucallback)
  * [createButton(options)](#createbuttonoptions)
* [Dialogs](#dialogs)
  * [showNoticeDialog(params)](#shownoticedialogparams)
  * [showConfirmDialog(params)](#showconfirmdialogparams)
  * [showLoadChartDialog()](#showloadchartdialog)
  * [showSaveAsChartDialog()](#showsaveaschartdialog)
* [Getters](#getters)
  * [symbolInterval(callback)](#symbolinterval)
  * [mainSeriesPriceFormatter()](#mainseriespriceformatter)
  * [getIntervals()](#getintervals)
  * [getStudiesList()](#getstudieslist)
  * [undoRedoState()](#undoredostate)
  * [getTheme()](#gettheme)
* [Customization](#customization)
  * [changeTheme(themeName, options)](#changethemethemename-options)
  * [addCustomCSSFile(url)](#addcustomcssfileurl)
  * [applyOverrides(overrides)](#applyoverridesoverrides)
  * [applyStudiesOverrides(overrides)](#applystudiesoverridesoverrides)
* :chart: [Trading Terminal only](#chart-trading-terminal-only)
  * [watchList()](#chart-watchlist)
* :chart: [Multiple Charts Layout](#chart-multiple-charts-layout)
  * [chart(index)](#chart-chartindex)
  * [activeChart()](#chart-activechart)
  * [chartsCount()](#chart-chartscount)
  * [layout()](#chart-layout)
  * [setLayout(layout)](#chart-setlayoutlayout)
  * [layoutName()](#chart-layoutName)
  * [symbolSync()](#chart-symbolsync)
  * [intervalSync()](#chart-intervalsync)
  * [crosshairSync()](#chart-crosshairsync)
  * [timeSync()](#chart-timesync)

## Subscribing To Chart Events

### onChartReady(callback)

1. `callback`: function()

The Charting Library will call the callback function 1 time when chart is initialized.
You can safely call all other methods starting from this moment.

### headerReady()

Returns a `Promise` object that should be used to handle an event when the Charting Library header widget API is ready (e.g. [createButton](#createbuttonoptions)).
The `Promise` object became available in 2015 which is why some older browsers, such as Internet Explorer do not support it. The Charting Library contains polyfills inside the iFrame only. Therefore, if you want to use this method in IE11, you should be adding the `Promise` polyfill.

### onGrayedObjectClicked(callback)

1. `callback`: function(subject)
    1. `subject`: object `{type, name}`
        * `type`: `drawing` | `study`
        * `name`: string, name of a clicked subject

The Library will call the `callback` function every time a user clicks on a grayed out object.

Example:

```javascript
new TradingView.widget({
    drawings_access: {
        type: "black",
        tools: [
            { name: "Trend Line" },
            { name: "Trend Angle", grayed: true },
        ]
    },
    studies_access: {
        type: "black",
        tools: [
            { name: "Aroon" },
            { name: "Balance of Power", grayed: true },
        ]
    },
    <...> // other widget settings
});

widget.onChartReady(function() {
    widget.onGrayedObjectClicked(function(data) {
        // this function will be called when a user tries to
        // create the Balance Of Power study or the Trend Angle shape

        alert(data.name + " is grayed out!");
    })
});
```

### onShortcut(shortcut, callback)

1. `shortcut`
1. `callback`: function(data)

The Library will call the `callback` function every time the shortcut key is pressed.

Example:

```javascript
widget.onShortcut("alt+s", function() {
  widget.chart().executeActionById("symbolSearch");
});
```

### subscribe(event, callback)

1. `event`: can be

| Event name | Library Version | Description |
|------------|-----------------|-------------|
| `toggle_sidebar` | | Drawing toolbar is shown/hidden |
| `indicators_dialog` | | Indicators dialog is shown |
| `toggle_header` | | Chart header is shown/hidden |
| `edit_object_dialog` | | Chart/Study Properties dialog is shown |
| `chart_load_requested` | | New chart is about to be loaded |
| `chart_loaded` | | |
| `mouse_down` | | |
| `mouse_up` | | |
| `drawing` | 1.7 | A drawing is added to a chart. The arguments contain an object with the `value` field that corresponds with the name of the drawing. |
| `study` | 1.7 | An indicator is added to a chart. The arguments contain an object with the `value` field that corresponds with the name of the indicator. |
| `undo` | 1.7 | |
| `redo` | 1.7 | |
| `undo_redo_state_changed` | 1.14 | The Undo/Redo state has been changed. The arguments contain an object with the state of the Undo/Redo stack. This object has the same structure as the result of [UndoRedoState](Widget-Methods.md#undoredostate) method |
| `reset_scales` | 1.7 | Reset scales button is clicked |
| `compare_add` | 1.7 | A compare dialog is shown |
| `add_compare` | 1.7 | A compare instrument is added |
| `load_study` template | 1.7 | A study template is loaded |
| `onTick` | | Last bar is updated |
| `onAutoSaveNeeded` | | User changed the chart. `Chart change` means any user action that can be undone. The callback function will not be called more than once every 5 seconds. See also [auto_save_delay](Widget-Constructor.md#auto_save_delay) |
| `onScreenshotReady` | | A screenshot URL is returned by the server |
| `onMarkClick` | | User clicked a [mark on a bar](Marks.md#marks-on-bars). Mark ID will be passed as an argument |
| `onPlusClick` | | User clicked the "plus" button on the price scale. The callback function will receive an object containing coordinates, `price` and `symbol` |
| `onTimescaleMarkClick` | | User clicked a [timescale mark](Marks.md#marks-on-the-timescale). Mark ID will be passed as an argument |
| `onSelectedLineToolChanged` | | Selected line tool is changed |
| `study_event` | 1.15 | An event related to the study. The callback function receives two arguments: a study ID and an event type (currently possible values for this argument are `remove` and at version 16 - `price_scale_changed`) |
| `series_event` | 16 | An event related to the series. The callback function receives an argument - an event type (currently the only possible value for this argument is `price_scale_changed`) |
| `drawing_event` | 1.15 | Drawing was hidden, shown, moved, removed, or clicked. The callback function will receive two arguments: a drawing ID and an event type. Possible values of the event type argument are `hide`, `show`, `move`, `remove`, `click` |
| `study_properties_changed` | 1.14 | Study properties are changed. Entity ID will be passed as an argument |
| `series_properties_changed` | 1.15 | Main series properties are changed. |
| `panes_height_changed` | 1.15 | Panes' size is changed. |
| `panes_order_changed` | 1.15 | Panes' order is changed. |
| :chart: `layout_about_to_be_changed` | | Amount or placement of the charts is about to be changed |
| :chart: `layout_changed` | | Amount or placement of the charts is changed |
| :chart: `activeChartChanged` | | Active chart is changed |

1. `callback`: function(arguments)

The library will call the `callback` function when a GUI `event` has happened.
Every event can have a different set of arguments.

### unsubscribe(event, callback)

Unsubscribes a previously subscribed `callback` function from a given `event` (that is one of the events in the table above).

## Chart Actions

### chart()

Returns a chart object that you can use to call [Chart-Methods](Chart-Methods.md)

### getLanguage()

*Starting from version 17.*

Returns the [language](Localization.md) of the widget.

### setSymbol(symbol, interval, callback)

1. `symbol`: string
1. `interval`: string
1. `callback`: function()

Changes the symbol and resolution of the chart. The `callback` function is called only when new symbol's data has been received.

### remove()

Removes the chart widget from the web page.

### closePopupsAndDialogs()

Calling this method closes all context menus, pop-ups or dialogs.

### selectLineTool(drawingId)

1. `drawingId`: may be one of the [identifiers](Shapes-and-Overrides.md) or
    1. `cursor`
    1. `dot`
    1. `arrow_cursor`
    1. `eraser`
    1. `measure`
    1. `zoom`
    1. `brush`

Selects a drawing or a cursor. It's the same as a single click on a drawing button.

### selectedLineTool()

Returns an [identifier](Shapes-and-Overrides.md) of the selected drawing or cursor (see above).

### takeScreenshot()

This method creates a snapshot of the chart and uploads it to the server.
When it is done the [onScreenshotReady](#subscribeevent-callback) callback function is called.
The URL of the snapshot will be passed as an argument to the callback function.

### takeClientScreenshot(options)

This method takes a snapshot of the chart layout and returns it as an HTML canvas element in a `Promise`.

`options` is an *optional* object that has the following fields:

* `backgroundColor`: background color
* `font`: legend text font family
* `fontSize`: legend text font size
* `legendMode`: `vertical` or `horizontal`
* `hideResolution`: if true resolution of the chart is hidden

### lockAllDrawingTools()

This method returns a [WatchedValue](WatchedValue.md) object that can be used to read/set/watch the state of Lock All Drawing Tools button.

### hideAllDrawingTools()

This method returns a [WatchedValue](WatchedValue.md) object that can be used to read/set/watch the state of Hide All Drawing Tools button.

### magnetEnabled()

This method returns a [WatchedValue](WatchedValue.md) object that can be used to read/set/watch the state of the Magnet (enabled - `true` or disabled - `false`).

### magnetMode()

This method returns a [WatchedValue](WatchedValue.md) object that can be used to read/set/watch the mode of the Magnet.

Available modes:

* `0` - weak magnet mode
* `1` - strong magnet mode

### startFullscreen()

This method enters full-screen mode.

### exitFullscreen()

This method exits full-screen mode.

## Saving/Loading Charts

### save(callback)

1. `callback`: function(object)

Saves the chart state to JS object. Charting Library will call your callback function and pass the state object as an argument.

This call is part of the low-level [save/load API](Saving-and-Loading-Charts.md).

### load(state)

1. `state`: object

Loads the chart from the `state` object. This call is part of the low-level [save/load API](Saving-and-Loading-Charts.md).

### getSavedCharts(callback)

1. `callback`: function(objects)

`objects` is an array of:

* `id`
* `name`
* `image_url`
* `modified_iso`
* `short_symbol`
* `interval`

Returns a list of chart descriptions saved to the server for the current user.

### loadChartFromServer(chartRecord)

1. `chartRecord` is an object that you get using [getSavedCharts(callback)](#getsavedchartscallback)

Loads and displays a chart from the server.

### saveChartToServer(onCompleteCallback, onFailCallback, options)

1. `onCompleteCallback`: function()
1. `onFailCallback`: function()
1. `options`: object `{ chartName }`
    * `chartName`: name of a chart. Should be specified for new charts and when renaming the chart.
    * `defaultChartName`: default name of a chart. It will be used if the current chart has no name.

Saves the current chart to the server.

### removeChartFromServer(chartId, onCompleteCallback)

1. `chartId`: the `id` should be received from the object that is returned by the [getSavedCharts(callback)](#getsavedchartscallback)
1. `onCompleteCallback`: function()

Removes the chart from the server.

## Custom UI Controls

### onContextMenu(callback)

1. `callback`: function(unixtime, price).
    This callback function is expected to return a value (see below).

The Charting Library will call the callback function every time  user opens a context menu on the chart.
The arguments that are passed to the callback function contain unix time and price of the clicked point on the chart.

You have to return an array of objects that have the following format to add or remove items from the context menu.

```javascript
{
    position: 'top' | 'bottom',
    text: 'Menu item text',
    click: <onItemClicked callback>
}
```

* `position`: position of the item in the context menu
* `text`: menu item text
* `click`: a callback function that will be called when a user selects your menu item

Use the minus sign to add a separator. Example: `{ text: "-", position: "top" }`.

Use the minus sign in front of the item text to remove an existing item from the menu.

Example:

```javascript
widget.onChartReady(function() {
    widget.onContextMenu(function(unixtime, price) {
        return [{
            position: "top",
            text: "First top menu item, time: " + unixtime + ", price: " + price,
            click: function() { alert("First clicked."); }
        },
        { text: "-", position: "top" },
        { text: "-Objects Tree..." },
        {
            position: "top",
            text: "Second top menu item 2",
            click: function() { alert("Second clicked."); }
        }, {
            position: "bottom",
            text: "Bottom menu item",
            click: function() { alert("Third clicked."); }
        }];
    });
```

### createButton(options)

1. `options`: object `{ align: "left" }`
    * `align`: `right` | `left`. default: `left`

Creates a new DOM element in the top toolbar of the chart and returns [HTMLElement](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement) for this button.
You can use it to add custom controls right on the chart.

**NOTE:** This method MUST be called after [headerReady](#headerready) promise is resolved.

Example:

```javascript
widget.headerReady().then(function() {
    var button = widget.createButton();
    button.setAttribute('title', 'My custom button tooltip');
    button.addEventListener('click', function() { alert("My custom button pressed!"); });
    button.textContent = 'My custom button caption';
});
```

## Dialogs

*Starting from version 1.6.*

### showNoticeDialog(params)

1. `params`: object:
    * `title`: text to be shown in the title
    * `body`: text to be shown in the body
    * `callback`: function to be called when ok button is pressed

This method shows a dialog with custom title and text along with the "OK" button.

### showConfirmDialog(params)

1. `params`: object:
    * `title`: text to be shown in the title
    * `body`: text to be shown in the body
    * `callback(result)`: function to be called when ok button is pressed.
        `result` is `true` if `OK` is pressed, otherwise it is `false`.

This method shows a dialog with the custom title and text along with the "OK" and "CANCEL" buttons.

### showLoadChartDialog()

Displays the "Load chart layout" dialog.

### showSaveAsChartDialog()

Displays the "Copy chart layout" dialog.

## Getters

### symbolInterval()

Charting Library returns an object that contains the symbol and interval of the chart.

### mainSeriesPriceFormatter()

Returns an object with the `format` method that you can use to format the prices. This was introduced in version 1.5.

### getIntervals()

Returns an array of supported resolutions. This was introduced in version 1.7.

### getStudiesList()

Returns an array of IDs of all studies. They can be used to create a study.

### undoRedoState()

Returns an object with the state of the Undo/Redo stack. The object has the following keys:

* `enableUndo`: boolean flag that shows the undo action availability
* `undoText`: name of the next undo operation. If the undo stack is empty then it is undefined.
* `enableRedo`: boolean flag that shows the redo action availability
* `redoText`: name of the next redo operation. If the redo stack is empty then it is undefined.

### getTheme()

*Starting from version 16.*

This method returns the chart theme name.

```javascript
console.log(widget.getTheme());
```

## Customization

### changeTheme(themeName, options)

*Starting from version 1.13.*

1. `themeName` should be `"Light"` | `"Dark"`
1. `options` is an *optional* object added in version 17 with one field:
    * `disableUndo` - boolean flag that shows the undo action availability.

This method changes the chart theme without reloading the chart.

You can also use the [theme](Widget-Constructor.md#theme) in the Widget Constructor to create the chart with a custom theme.

### addCustomCSSFile(url)

1. `url` should be an absolute or relative path to the `static` folder

This method was introduced in version `1.3`.

Starting from version `1.4` use [custom_css_url](Widget-Constructor.md#custom_css_url) instead.

### applyOverrides(overrides)

*Starting from version 1.5.*

1. `overrides` is an object.
    It is the same as [overrides](Widget-Constructor.md#overrides) in the Widget Constructor.

This method applies "overrides" to the properties without reloading the chart.

### applyStudiesOverrides(overrides)

*Starting from version 1.9.*

1. `overrides` is an object. It is the same as [studies_overrides](Widget-Constructor.md#studies_overrides) in the Widget Constructor.

This method applies "overrides" to the styles or inputs of the indicators without reloading the chart.

## :chart: Trading Terminal only

The following methods are available in [Trading Terminal](Trading-Terminal.md) only.

### :chart: watchList()

*Starting from version 1.9.*

Returns an object to manage the watchlist. The object has the following methods:

1. `defaultList()` - allows you to get a default list of symbols.

1. `getList(id?: string)` - allows you to get a list of symbols. If the `id` parameter is not provided then the current list will be returned. If there is no WatchList then `null` will be returned.

1. `setActiveList(id: string)` - allows you to make a list with the `id` active.

1. `getActiveListId()` - allows you to get the ID of the current list. If there is no WatchList then `null` will be returned.

1. `getAllLists()` - allows you to get all lists. If there is no WatchList then `null` will be returned.

1. `setList(symbols: string[])` - allows you to set a list of symbols into the watchlist. It will replace the entire list. **Obsolete. Will be removed in version `1.13`. Use `updateList` instead.**

1. `updateList(listId: string, symbols: string[])` - allows you to edit the list of symbols.

1. `renameList(listId: string, newName: string)` - allows you to rename the list to `newName`.

1. `createList(listName?: string, symbols?: string[])` - allows you to create a list of symbols with `listName` name. If the `listName` parameter is not provided or there is no WatchList then `null` will be returned;

1. `saveList(list: SymbolList)` - allows you to save a list of symbols where `list` is an object with the following keys:

    ```js
    id: string;
    title: string;
    symbols: string[];
    ```

    If there is no WatchList or an equivalent list already exists then `false` will be returned, otherwise `true` will returned.

1. `deleteList(listId: string)` - allows you to delete a list of symbols.

1. `onListChanged(listId: string)` - you can use this method to be notified when the symbols of the active watchlist are changed. You can subscribe and unsubscribe using the [[Subscription]] object returned by this function.

1. `onActiveListChanged()` - you can use this method to be notified when a different list of the watchlist is selected. You can subscribe and unsubscribe using the [[Subscription]] object returned by this function.

1. `onListAdded()` - - you can use this method to be notified when the new list is added to the watchlist. You can subscribe and unsubscribe using the [[Subscription]] object returned by this function.

1. `onListRemoved()` - you can use this method to be notified when the list is removed from the watchlist. You can subscribe and unsubscribe using the [[Subscription]] object returned by this function.

1. `onListRenamed()` - - you can use this method to be notified when the list is renamed in the watchlist. You can subscribe and unsubscribe using the [[Subscription]] object returned by this function.

## :chart: Multiple Charts Layout

### :chart: chart(index)

1. `index`: index of a chart starting from `0`. `index` is `0` by default.

Returns a chart object that you can use to call [Chart-Methods](Chart-Methods.md)

### :chart: activeChart()

Returns a chart object of the active chart that you can use to call [Chart-Methods](Chart-Methods.md)

### :chart: chartsCount()

Returns the amount of charts in the current layout.

### :chart: layout()

Returns the current layout mode. Possible values are: `4`, `6`, `8`, `s`, `2h`, `2-1`, `2v`, `3h`, `3v`, `3s`, `1-2`, `3r`, `4h`, `4v`, `4s`, `1-3`, `2-2`, `1-4`, `5s`, `6c`, `8c`.

### :chart: setLayout(layout)

1. `layout`: Possible values are: `4`, `6`, `8`, `s`, `2h`, `2-1`, `2v`, `3h`, `3v`, `3s`, `1-2`, `3r`, `4h`, `4v`, `4s`, `1-3`, `2-2`, `1-4`, `5s`, `6c`, `8c`.

Changes the current chart layout.

### :chart: layoutName()

Returns the current layout name. If the current layout has not yet been saved then it returns undefined.

### :chart: symbolSync()

Returns a [WatchedValue](WatchedValue.md) object that can be used to read/set/watch the state of symbol sync between charts.

```javascript
if (widget.symbolSync().value()) {
    // Do something
}
```

### :chart: intervalSync()

Returns a [WatchedValue](WatchedValue.md) object that can be used to read/set/watch the state of interval sync between charts.

```javascript
widget.intervalSync().setValue(true);
```

### :chart: crosshairSync()

Returns a [WatchedValue](WatchedValue.md) object that can be used to read/set/watch the state of crosshair sync between charts.

```javascript
widget.crosshairSync().setValue(true);
```

### :chart: timeSync()

Returns a [WatchedValue](WatchedValue.md) object that can be used to read/set/watch the state of time sync between charts.

```javascript
widget.timeSync().setValue(true);
```

## See Also

* [Chart-Methods](Chart-Methods.md)
* [Widget Constructor](Widget-Constructor.md)
* [Saving and Loading Charts](Saving-and-Loading-Charts.md)
* [Overriding Default Properties of the Studies](Studies-Overrides.md)
* [Overriding Default Properties of the Chart](Overrides.md)
