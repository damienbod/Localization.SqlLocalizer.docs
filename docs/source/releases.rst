Release History
============

.. note::
    Current Version using ASP.NET Core 1.1, EFCore 1.1


Version 1.0.6
-------------
* return default key if localization cannot be found support

Example

.. highlight:: guess
	var useTypeFullNames = true;
	var useOnlyPropertyNames = false;
	var returnOnlyKeyIfNotFound = true;

	services.AddSqlLocalization(options => options.UseSettings(
	  useTypeFullNames, 
	  useOnlyPropertyNames, 
	  returnOnlyKeyIfNotFound
	));

Version 1.0.5
-------------

* bugfix context System.InvalidOperationException import, export

Version 1.0.4
-------------

* Updated to .NET Core 1.1
* changed the constraint to included the resourceKey for new records

Version 1.0.3
-------------

* adding import, export interfaces

Version 1.0.2
-------------

* Updated to dotnet RTM

Version 1.0.1
-------------

* Added Unique constraint for key, culture
* Fixed type full name cache bug

Version 1.0.0
-------------

* Initial release
* Runtime localization updates
* Cache support, reset cache
* ASP.NET DI support
* Supports any Entity Framework Core database
