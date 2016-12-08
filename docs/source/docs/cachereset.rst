Cache Reset, live updates
=======================================

If you decide to update the localization data directly in the database, you can reset the application localization cache using the ResetCache methods from the IStringExtendedLocalizerFactory interface.

By using these methods, the application does not need to be restarted to update the localization values.

IStringExtendedLocalizerFactory ResetCache methods
-----------------------


.. highlight:: csharp

::

    public interface IStringExtendedLocalizerFactory : IStringLocalizerFactory
    {
        void ResetCache();

        void ResetCache(Type resourceSource);