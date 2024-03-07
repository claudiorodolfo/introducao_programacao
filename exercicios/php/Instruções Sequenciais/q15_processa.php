<?php
	$preco = $_POST['preco'];

	if ($preco < 20)
		print 'Preço de Venda:'. ($preço * 1.4);
	else
		print 'Preço de Venda:'. ($preço * 1.3);
?>