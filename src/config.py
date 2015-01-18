from authomatic.providers import oauth2, oauth1, openid, gaeopenid
import authomatic

CONFIG = {

    'tw': { # Your internal provider name

        # Provider class
        'class_': oauth1.Twitter,
        # 'short_name': 4,
        # Twitter is an AuthorizationProvider so we need to set several other properties too:
        'consumer_key': 'CUSTOMER',
        'consumer_secret': 'SECRET',
        'id': authomatic.provider_id(),
    },

    'fb': {

        'class_': oauth2.Facebook,
        # 'short_name': 1, # Unique value used for serialization of credentials only needed by OAuth 2.0 and OAuth 1.0a.
        # Facebook is an AuthorizationProvider too.
        'consumer_key': 'CUSTOMER',
        'consumer_secret': 'SECRET',
        'id': authomatic.provider_id(),

        # But it is also an OAuth 2.0 provider and it needs scope.
        'scope': ['user_about_me', 'email', 'publish_stream', 'offline_access'],
    },
    # 'google': {
    #      'class_': 'authomatic.providers.oauth2.Google', # Can be a fully qualified string path.
    #
    #      # Provider type specific keyword arguments:
    #      'short_name': 2, # use authomatic.short_name() to generate this automatically
    #      'consumer_key': '###################',
    #      'consumer_secret': '###################',
    #      'scope': ['https://www.googleapis.com/auth/userinfo.profile',
    #                'https://www.googleapis.com/auth/userinfo.email']
    # },
    'oi': {

        # OpenID provider dependent on the python-openid package.
        'class_': openid.OpenID,
        'store': openid.SessionOpenIDStore,
    },
    # 'google_oi': {
    #      'class_': openid.Google, # OpenID provider with predefined identifier 'https://www.google.com/accounts/o8/id'.
    # },
    'gaeoi': {
         'class_': gaeopenid.GAEOpenID, # Google App Engine based OpenID provider.
    }
}