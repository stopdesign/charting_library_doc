:chart: All content on this page applies to the [Trading Terminal](Trading-Terminal.md) only.

Trading Host is an API for interaction between [Broker API](Broker-API.md) and the Chart Trading Subsystem. Its main purpose is to exchange information between our charts and your trading adapter. In terms of `JS`, it is an `object` with a set of functions. Here is the list of Hosts's **methods**.

## Commands

### showOrderDialog(order, focus) : Promise

1. `order` to be placed or modified
1. `focus` - [Focus constant](Trading-Objects-and-Constants.md#orderticketfocuscontrol).

Shows standard Order Dialog to create or modify an order and executes handler if Buy/Sell/Modify is pressed.

### showCancelOrderDialog(orderId, handler) : Promise

1. `orderId` ID of an order to be cancelled
1. `handler` is a function to process cancellation. It should return Promise

Shows a confirmation dialog and executes handler if YES/OK is pressed.

### showCancelMultipleOrdersDialog(symbol, side, qty, handler) : Promise

1. `symbol` of orders to be cancelled
1. `side` - side of orders to be cancelled
1. `qty` - amount of orders to be cancelled
1. `handler` is a function to process cancellation. It should return Promise

Shows a confirmation dialog and executes handler if YES/OK is pressed.

### showReversePositionDialog([position](Trading-Objects-and-Constants.md#position), handler) : Promise

1. `position` to be reversed
1. `handler` is a function to process position reverse. It should return a Promise

Shows a confirmation dialog and executes handler if YES/OK is pressed.

### showPositionBracketsDialog([position](Trading-Objects-and-Constants.md#position), [brackets](Trading-Objects-and-Constants.md#brackets), focus) : Promise

1. `position` to be modified
1. `brackets` (optional) new [brackets](Trading-Objects-and-Constants.md#brackets)
1. `focus` - [Focus constant](Trading-Objects-and-Constants.md#orderticketfocuscontrol).

Shows a default edit brackets dialog and executes handler if MODIFY is pressed.

### activateBottomWidget : Promise

Opens the bottom panel and switches the tab to Trading.

### showTradingProperties()

Shows the properties dialog, switches current tab to Trading.

### showNotification(title, text, type)

Displays a notification. Type can be `1` - success or `0` - error.

### triggerShowActiveOrders()

Triggers show active orders.

### numericFormatter(decimalPlaces)

Returns a [Formatter](Trading-Objects-and-Constants.md#formatter) with the specified number of decimal places.

### defaultFormatter(symbol: string, alignToMinMove?: boolean = true)

Returns a default [Formatter](Trading-Objects-and-Constants.md#formatter) formatter for the specified instrument. This formatter is created based on [SymbolInfo](Symbology.md#symbolinfo-structure).

By default, the formatter rounds a price to the minimum price movement, but sometimes you may want to disable this rounding. For example, the average price of a position should not be rounded to the minimum price movement. Let’s assume that we placed one trade at `100.25` and another trade at `100.50`. The average price of the position is going to be `100.375`. If you get a formatter using `defaultFormatter(symbol)`, then this formatter will round this price to `100.38`, but if you set the second argument to `false`, then the price will be rounded to `100.50`.

### factory

`factory` is an object property. Its functions are described below.

### factory.createDelegate

Creates a [Delegate](Delegate.md) object.

### factory.createWatchedValue

Creates a [WatchedValue](WatchedValue.md) object.

### factory.createPriceFormatter(priceScale, minMove, fractional, minMove2)

Creates a price [Formatter](Trading-Objects-and-Constants.md#formatter). The arguments of this function are described in [another article](Symbology.md#minmov-pricescale-minmove2-fractional).

### symbolSnapshot(symbol) : Promise

Returns quotes of a symbol.

## Getters and Setters

### sellBuyButtonsVisibility: [WatchedValue](WatchedValue.md)

Returns whether the buy/sell buttons are visible or not.

### domVisibility: [WatchedValue](WatchedValue.md)

Returns whether DOM is visible or not.

### orderPanelVisibility: [WatchedValue](WatchedValue.md)

Returns whether the order panel is visible or not.

### showPricesWithZeroVolume: [WatchedValue](WatchedValue.md)

Returns whether levels with empty volume (between min and max volume levels) are collapsed or not.

### silentOrdersPlacement: [WatchedValue](WatchedValue.md)

Returns if orders can be sent to the broker without showing the order ticket.

### suggestedQty() : Object

Returned object properties:

1. value - use it to get the current value. It returns Promise.
1. setValue - use it to set new value
1. changed : [Subscription](Subscription.md)

It is to synchronize quantity in the Floating Trading Panel and in the dialogs.

### setButtonDropdownActions(actions)

Bottom Trading Panel has a button with a list of dropdown items. This method can be used to replace existing items.

1. `actions` is an array of [ActionMetaInfo](Trading-Objects-and-Constants.md#actionmetainfo), each of them representing one dropdown item.

### defaultContextMenuActions()

Provides default buy/sell, show properties actions to be returned as a default by [chartContextMenuActions](Broker-API.md#chartcontextmenuactionse).

### defaultDropdownMenuActions(options)

Provides default dropdown list of actions. You can use default actions in [setButtonDropdownActions](#setButtonDropdownActionsactions).
You can add/remove default action from the result using `options`:

1. `showSellBuyButtons`: boolean;
1. `tradingProperties`: boolean;
1. `showDOM`: boolean;
1. `showOrderPanel`: boolean;

## Data Updates

The usage of these methods is required to notify the chart that it needs to update information.

### orderUpdate([order](Trading-Objects-and-Constants.md#order))

Call this method when an order is added or changed.

### orderPartialUpdate([order](Trading-Objects-and-Constants.md#order))

Call this method when an order is not changed, but the fields that you added to the order object to display in the Account Manager are changed.
It should be used only if you want to display custom fields in the [Account Manager](Account-Manager.md).

### positionUpdate ([position](Trading-Objects-and-Constants.md#position))

Call this method when a position is added or changed.

### positionPartialUpdate ([position](Trading-Objects-and-Constants.md#position))

Call this method when a position is not changed, but fields that you added to the position object to display in the Account Manager are changed.
It should be used only if you want to display custom fields in the [Account Manager](Account-Manager.md).

### executionUpdate([execution](Trading-Objects-and-Constants.md#execution))

Call this method when an execution is added.

### currentAccountUpdate()

Call this method when user account has been changed synchronously. The terminal will re-request all displayed information.

### plUpdate(positionId, pl)

Call this method when a broker connection has received a PL update. This method should be used when `supportPLUpdate` flag is set in `configFlags`.

### equityUpdate(equity)

Call this method when a broker connection has received an equity update. This method is required by the standard Order Dialog to calculate risks.

### marginAvailableUpdate(marginAvailable)

Call this method when a broker connection has received a margin available update. This method is required by the standard Order Dialog to display the margin meter. This method should be used when `supportMargin` flag is set in `configFlags`. The Trading Terminal subscribes to margin available updates using [subscribeMarginAvailable](Broker-API.md#subscribemarginavailable).

### cryptoBalanceUpdate(balance)

Call this method when a broker connection has received a balance update. This method is required by the crypto Order Dialog. It should be implemented when `supportBalances` flag is set in `configFlags`.

### tradeUpdate ([trade](Trading-Objects-and-Constants.md#trade))

Call this method when a trade is added or changed.

### tradePartialUpdate ([trade](Trading-Objects-and-Constants.md#trade))

Call this method when a trade is not changed, but fields that you added to the trade object to display in the Account Manager are changed.

### tradePLUpdate(tradeId, pl)

Call this method when a broker connection has received a trade PL update.

### pipValueUpdate(symbol, pipValues)

Call this method when a broker connection has a `pipValue` update. The library subscribes to `pipValue` updates using [subscribePipValue](Broker-API.md#subscribepipvalue).

`pipValues` is an object with the following fields:

1. `buyPipValue` - value of 1 pip if you buy `symbol`
1. `sellPipValue` - value of 1 pip if you sell `symbol`
