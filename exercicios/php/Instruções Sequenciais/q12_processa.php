<?php
	$mes = $_POST['mes'];
	$ano = $_POST['ano'];
	
	switch($mes) {
		case 2:
			if (($ano % 4 == 0 && $ano % 100 != 0) || $ano % 400 == 0)
				print '29 dias!';
			else
				print '28 dias!';
			
			break;
		case 1:
		case 3:
		case 5:
		case 7:
		case 8:
		case 10:
		case 12:
			print '31 dias!';
			break;
		case 4:
		case 6:
		case 9:
		case 11:
			print '30 dias!';
			break;
	}
?>