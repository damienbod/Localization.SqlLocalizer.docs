Configuration 
=======================================

The following configurations can be set in the ConfigureServices method in the Startup.cs file.

.. highlight:: csharp

The LocalizationModelContext needs to be added to the services. You need to then decide which database is to be used. Because the context is in a separate assembly, if you are using migrations, you need to define the MigrationsAssembly property.

ConfigureServices in the Startup.cs::

	public void ConfigureServices(IServiceCollection services)
	{
		// init database for localization
		var sqlConnectionString = Configuration["DbStringLocalizer:ConnectionString"];

		services.AddDbContext<LocalizationModelContext>(options =>
			options.UseSqlite(
				sqlConnectionString,
				b => b.MigrationsAssembly("Angular2LocalizationAspNetCore")
			)
		);

		// Requires that LocalizationModelContext is defined
		services.AddSqlLocalization(options => options.UseTypeFullNames = true);


Default
-----------------------

.. highlight:: csharp

Uses the Name property of the class type to create the key::

	services.AddSqlLocalization();


Using full types as keys
-----------------------

.. highlight:: csharp

Uses the FullName of the class type to create the key::

	services.AddSqlLocalization(options => options.UseTypeFullNames = true);


Using only property names
-----------------------

.. highlight:: csharp

Uses only the property name for the key::

	services.AddSqlLocalization(options => options.UseOnlyPropertyNames = true);


Displaying default keys
-----------------------

.. highlight:: csharp

Display default keys when localization is undefined::

	var useTypeFullNames = true;
	var useOnlyPropertyNames = false;
	var returnOnlyKeyIfNotFound = true;

	services.AddSqlLocalization(options => options.UseSettings(
	  useTypeFullNames, 
	  useOnlyPropertyNames, 
	  returnOnlyKeyIfNotFound
	));
