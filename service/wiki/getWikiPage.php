<?php
header('Access-Control-Allow-Origin: *');
$response = array("title" => "");

function getResult($category){
	$cmd = "sh get.sh " . $category;
	$result = shell_exec($cmd);
	return explode("\n", $result);
}

$response["title"] = getResult($_GET["category"]);

echo json_encode($response);

exit;