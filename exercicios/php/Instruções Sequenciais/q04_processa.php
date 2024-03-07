<?php
	$nome = $_POST['nome'];
	$nota1 = $_POST['nota1'];
	$nota2 = $_POST['nota2'];
	$nota3 = $_POST['nota3'];
	$media = 3 / (1/$nota1 + 1/$nota2 + 1/$nota3);
	print 'A média harmônica é ' . $media;
?>