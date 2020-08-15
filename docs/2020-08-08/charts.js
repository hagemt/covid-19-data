/* eslint-env browser */
/* global google */

const version1 = {
	date: '2020-08-08',
	rows: [
		['State', '% positive tests'],
['Alabama',17.64],
['Alaska',1.71],
['Arizona',15.53],
['Arkansas',11.50],
['California',5.70],
['Colorado',7.18],
['Connecticut',0.72],
['Delaware',4.78],
['Florida',17.74],
['Georgia',12.69],
['Hawaii',6.65],
['Idaho',16.09],
['Illinois',4.10],
['Indiana',8.75],
['Iowa',9.57],
['Kansas',11.77],
['Kentucky',6.73],
['Louisiana',7.66],
['Maine',0.62],
['Maryland',5.71],
['Massachusetts',2.74],
['Michigan',2.55],
['Minnesota',6.22],
['Mississippi',20.45],
['Missouri',10.70],
['Montana',4.45],
['Nebraska',8.96],
['Nevada',17.37],
['New Hampshire',1.95],
['New Jersey',1.53],
['New Mexico',2.63],
['New York',0.96],
['North Carolina',5.84],
['North Dakota',7.31],
['Ohio',4.86],
['Oklahoma',9.58],
['Oregon',6.40],
['Pennsylvania',5.23],
['Rhode Island',5.99],
['South Carolina',12.25],
['South Dakota',8.56],
['Tennessee',8.63],
['Texas',16.20],
['Utah',10.53],
['Vermont',0.52],
['Virginia',8.16],
['Washington',13.68],
['West Virginia',2.76],
['Wisconsin',6.16],
['Wyoming',8.24],
	],
}

const version2 = {
	date: '2020-08-15',
	rows: [
		['State', '% positive tests'],
['Alabama',10.60],
['Alaska',2.15],
['Arizona',10.63],
['Arkansas',11.72],
['California',6.53],
['Colorado',3.93],
['Connecticut',0.79],
['Delaware',7.05],
['Florida',17.15],
['Georgia',10.55],
['Hawaii',7.63],
['Idaho',16.56],
['Illinois',4.06],
['Indiana',9.19],
['Iowa',9.73],
['Kansas',12.24],
['Kentucky',7.68],
['Louisiana',6.05],
['Maine',0.47],
['Maryland',4.90],
['Massachusetts',1.79],
['Michigan',2.34],
['Minnesota',7.17],
['Mississippi',23.05],
['Missouri',10.94],
['Montana',6.48],
['Nebraska',9.05],
['Nevada',16.71],
['New Hampshire',1.36],
['New Jersey',1.75],
['New Mexico',2.63],
['New York',0.85],
['North Carolina',6.22],
['North Dakota',9.13],
['Ohio',5.04],
['Oklahoma',8.08],
['Oregon',5.58],
['Pennsylvania',5.12],
['Rhode Island',5.02],
['South Carolina',7.90],
['South Dakota',8.96],
['Tennessee',7.78],
['Texas',16.37],
['Utah',8.47],
['Vermont',0.82],
['Virginia',6.24],
//['Washington',100.0], // WTF is this? (definitely a mistake)
['West Virginia',2.63],
['Wisconsin',7.51],
['Wyoming',5.44],
	],
}

// https://developers.google.com/chart/interactive/docs/basic_load_libs#load-settings
google.charts.load('current', {
	mapsApiKey: 'AIzaSyD-9tSrke72PouQMnMX-a7eZSW0jkFMBWY',
	packages: ['geochart'],
});

google.charts.setOnLoadCallback(() => {
	const options = {
		colorAxis: {
			colors: ['green', 'red'],
		},
		displayMode: 'regions',
		region: 'US',
		resolution: 'provinces',
		sizeAxis: {
			maxValue: 100,
			minValue: 0,
		},
	}

	for (const { date, rows } of [version1, version2]) {
		const div = document.getElementById('r' + date);
		const chart = new google.visualization.GeoChart(div);
		const data = google.visualization.arrayToDataTable(rows);
		chart.draw(data, options);
	}
})

window.charts = Object.freeze({
	hide: (date) => {
		const charts = document.getElementById('charts');
		const chart = document.getElementById('s' + date);

		const btn = document.createElement('button');
		btn.innerHTML = 'Show ' + date;
		btn.onclick = () => {
			chart.style.display = 'block';
			charts.removeChild(btn);
			return false;
		}
		btn.style.display = 'block';

		chart.style.display = 'none';
		charts.appendChild(btn);
		return false;
	},
	hideAll: () => {
		for (const { date } of [version1, version2]) {
			window.charts.hide(date);
		}
		return false;
	},
	showAll: () => {
		location.reload();
	},
})
