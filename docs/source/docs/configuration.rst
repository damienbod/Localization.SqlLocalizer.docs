Configuration 
=======================================

.. highlight:: csharp

::

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
