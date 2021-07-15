var ctx = document.getElementById('myChart').getContext('2d');

console.log(labels)
console.log(values)

const data = {
    labels: labels,
    datasets: [
      {
        label: 'Count de WorkItems por Type',
        data: values,
        backgroundColor: [
            'rgba(255, 99, 132, 0.2)',
            'rgba(54, 162, 235, 0.2)',
            'rgba(255, 206, 86, 0.2)',
            'rgba(75, 192, 192, 0.2)',
            'rgba(153, 102, 255, 0.2)',
            'rgba(255, 159, 64, 0.2)'
        ],
        borderWidth: 1
      }
    ]
  };

const config = {
    type: 'pie',
    data: data,
    options: {
      responsive: true,
      plugins: {
        legend: {
          position: 'top',
        },
        title: {
          display: true,
          text: 'Chart.js Pie Chart'
        }
      }
    },
  };

var myChart = new Chart(ctx, config);