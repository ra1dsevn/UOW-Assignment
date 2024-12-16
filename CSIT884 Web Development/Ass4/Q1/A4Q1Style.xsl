<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        <html>
            <head>
                <style>
                    h1 {
                    font-size: 30px;
                    font-weight: bold;
                    }

                    strong {
                    font-weight: bold;
                    }
                </style>
            </head>
            <body>
                <h1>Login Report 2023/09/20</h1>
                <br/>
                <xsl:apply-templates select="report/device_name"/>
                <br/>
                <xsl:apply-templates select="report/user"/>
            </body>
        </html>
    </xsl:template>

    <xsl:template match="device_name">
        <p>
            <strong>Device name:</strong> <xsl:value-of select="."/>
        </p>
    </xsl:template>

    <xsl:template match="user">
        <p>
            <strong>Username:</strong> <xsl:value-of select="username"/>
        </p>
        <p>
            <strong>Name:</strong> <xsl:value-of select="name"/>
        </p>
        <p>
            <strong>Group:</strong> <xsl:value-of select="group"/>
        </p>
        <h3>
            <strong>Login:</strong>
        </h3>
        <br/>
        <ul>
            <xsl:apply-templates select="login/record"/>
        </ul>
        <br/>
    </xsl:template>

    <xsl:template match="record">
        <li>
            <xsl:value-of select="."/>
        </li>
    </xsl:template>
</xsl:stylesheet>