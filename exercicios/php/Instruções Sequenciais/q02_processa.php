<?php
	$valor1 = $_POST['valor1'];
	$valor2 = $_POST['valor2'];
	$media = $valor1 * 0.4 + $valor2 * 0.6;
	print 'A média ponderada é ' . $media;
?>