<?php
	$valor = $_POST['valor'];
	
	$parteInteira = intval($valor);
	print 'Parte Fracionada' . ($valor - $parteInteira)

?>