const quote = document.querySelector("#quote span:first-child");
const author = document.querySelector("#quote span:last-child");

fetch('data/quotes.json')
  .then(response => response.json())
  .then(quotes => {
    const todaysQuote = quotes[Math.floor(Math.random() * quotes.length)];
    quote.innerText = todaysQuote.quote;
    author.innerText = todaysQuote.author;
  });
