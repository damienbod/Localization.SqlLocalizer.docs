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
	  returnOnlyKeyIfNotFound,
	  false
	));

Development add resources automatically if not found
-----------------------

You should only use this feature in development. The env.IsDevelopment() method provides a good way to configure this.

.. highlight:: csharp

Add when undefined::

	private bool _createNewRecordWhenLocalisedStringDoesNotExist = false;

	public Startup(IHostingEnvironment env)
	{
		var builder = new ConfigurationBuilder()
			.SetBasePath(env.ContentRootPath)
			.AddJsonFile("appsettings.json", optional: true, reloadOnChange: true)
			.AddJsonFile($"appsettings.{env.EnvironmentName}.json", optional: true);

		builder.AddEnvironmentVariables();
		Configuration = builder.Build();

		if (env.IsDevelopment())
		{
			_createNewRecordWhenLocalisedStringDoesNotExist = true;
		}
	}
	
	public void ConfigureServices(IServiceCollection services)
    {
		var useTypeFullNames = false;
		var useOnlyPropertyNames = false;
		var returnOnlyKeyIfNotFound = false;


		services.AddSqlLocalization(options => options.UseSettings(
			useTypeFullNames, 
			useOnlyPropertyNames, 
			returnOnlyKeyIfNotFound,
			_createNewRecordWhenLocalisedStringDoesNotExist));

	

Setting the schema
-----------------------

.. highlight:: csharp

Set the SQL setting for the localization::

	services.AddLocalizationSqlSchema("translations");
	services.AddDbContext<LocalizationModelContext>(options =>
		options.UseSqlite(
			sqlConnectionString,
			b => b.MigrationsAssembly("AspNet5Localization")
		)
	);

