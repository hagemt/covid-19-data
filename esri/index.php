<!DOCTYPE html>
<head>
	<title>JHU Country Data JSON</title>
	<style type="text/css">
td, th {
	border: 1px solid black;
	margin: .2rem;
	padding: .3rem;
	text-align: right;
}
	</style>
</head>
<body>

<?php
$file = "example-ncov-data.json"; // from 1596928122000=2020-08-08T23:08:42.000Z
$when = strcmp($file, "example-ncov-data.json") !== 0 ? "latest" : "2020-08-08";

$json = file_get_contents($file); // array
$data = json_decode($json, true)["features"];

//foreach ($data as $datum): echo json_encode($datum["attributes"]); endforeach;
//$data = array(array("attributes" => array("key" => "foo", "value" => "bar")));
?>

	<main>
		<h1>JHU Country Data</h1>
		<p>From <?php echo ($when . ": " . $file); ?> file(s)</p>
	</main>

	<table>
	<thead>
		<tr>
		<th><?php echo implode('</th><th>', array_keys($data[0]["attributes"])); ?></th>
		</tr>
	</thead>
	<tbody>
<?php foreach ($data as $datum): array_map('htmlentities', $datum["attributes"]); ?>
		<tr>
			<td><?php echo implode('</td><td>', $datum["attributes"]); ?></td>
		</tr>
<?php endforeach; ?>
	</tbody>
	</table>

	<footer>
		<p><?php echo ('Data copyright &copy; ' . date('Y') . ' (code as licensed)');  ?></p>
	</footer>

</body>
