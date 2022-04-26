function usdToBgn(input) {
    let dollarExchangeRate = 1.79549

    let usd = Number(input[0])

    let bgn = usd * dollarExchangeRate

    console.log(bgn)
}

usdToBgn(["22"])
usdToBgn(["100"])
usdToBgn(["12.5"])
