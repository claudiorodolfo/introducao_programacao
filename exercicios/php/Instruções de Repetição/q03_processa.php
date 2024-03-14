<?php
	$numero = $_POST['valor'];
	//para
	for ($i = 1; $i <= $numero; $i++) {
		print $i . ' ';
	}
	print '<br><br>';
	//enquanto
	$j = 1;
	while($j <= $numero) {
		print $j . ' ';
		$j++;
	}
?>