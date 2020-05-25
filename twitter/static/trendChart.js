/**
 *
 * @param title
 * @param topics
 * @param volume
 */
function visualize_chart(title, topics, volume, id) {
    var ctx = document.getElementById(id).getContext('2d');
    var gradient = ctx.createLinearGradient(0, 0, 0, 400);
    gradient.addColorStop(0, 'blue');
    gradient.addColorStop(1, '#CCF2FF');
    var myChart = new Chart(ctx, {
        type: 'horizontalBar',
        data: {
            labels: Array.isArray(topics) ? topics : JSON.parse(topics),
            datasets: [{
                backgroundColor: gradient,
                label: 'tweet volume',
                data: Array.isArray(volume) ? volume :JSON.parse(volume),
                borderWidth: 0,
            }]
        },
        options: {
            responsiveAnimationDuration: 0,
            maintainAspectRatio: true,
            aspectRatio: 2,
            responsive: true,
            title: {
                display: true,
                text: title
            },
            legend: {
              display: false
            },
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
        }
    });
    return myChart
}
