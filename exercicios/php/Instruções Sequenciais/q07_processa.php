<?php
	$valor = $_POST['valor'];
	$resultado = number_format($valor, 2);
	print 'Resultado: ' . $resultado;
?>