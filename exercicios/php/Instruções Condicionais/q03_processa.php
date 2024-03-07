<?php
	$valor = $_POST['valor'];
	
	switch ($valor) {
	case 1:
	case 7:
		print 'Fim de Semana!';
		break;
	case 2:
	case 3:
	case 4:
	case 5:
	case 6:
		print 'Dia útil!';
		break;
	}
?>