for file in `find ./src -name \*.cpp -print` ; do
	echo "'${file}'",
done

for file in `find ./tools -name \*.cpp -print` ; do
	echo "'${file}'",
done

for file in `find ./build/src  -name \*.cc -print` ; do
	echo "'${file}'",
done
