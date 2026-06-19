#rom database import get_products

#products = get_products()
#rint(products)
#(3, 'bread', Decimal('60.00'), Decimal('65.00'))


#for i in products:
 #   print(i[1])


even = []
for i in range (50,201):
  if i%2 == 0:
   even.append(i)
print(even)
  new Chart(document.getElementById("line-chart"), {
  type: 'line',
  data: {
    labels: {{ dates| safe }},
    datasets: [{ 
        data: {{ day_profit | safe }},
        label: "Africa",
        borderColor: "#3e95cd",
        fill: false
      }, { 
        data: {{ day_sales | safe }},
        label: "Asia",
        borderColor: "#8e5ea2",
        fill: false
      },  
    ]
  },
  options: {
    title: {
      display: true,
      text: 'World population per region (in millions)'
    }
  }
});

new Chart(document.getElementById("bar-chart-grouped"), {
    type: 'bar',
    data: {
      labels: ["1900", "1950", "1999", "2050"],
      datasets: [
        {
          label: "Africa",
          backgroundColor: "#3e95cd",
          data: [133,221,783,2478]
        }, {
          label: "Europe",
          backgroundColor: "#8e5ea2",
          data: [408,547,675,734]
        }
      ]
    },
    options: {
      title: {
        display: true,
        text: 'Population growth (millions)'
      }
    }
});
